add_library( day25 day25.cpp)

target_include_directories(day25 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day25 TBB::tbb )