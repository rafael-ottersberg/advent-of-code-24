add_library( day22 day22.cpp)

target_include_directories(day22 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day22 TBB::tbb )