add_library( day05 day05.cpp)

target_include_directories(day05 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day05 TBB::tbb )